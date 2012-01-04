# configuring PYTHONPATH (By default, this will add the src and lib directory for each of your dependencies to your PYTHONPATH)
import roslib; roslib.load_manifest('sap_pkg')

# import client library
import rospy

# import messages
import auction_msgs.msg

# import services
import auction_srvs.srv

import auction_common

# import auxiliar libraries
import random
import math

# "global" variables (to be referred as global under def fun(something))
winner_id = 'none'
winner_cost = 0


#####################################################################################
## Buyer Service Callback
#####################################################################################
def handle_buyer_server_callback(auction_req):
    
    # Prepare information
    role = "be_buyer"
    auction_type = 'sap'
    sending_node = rospy.get_name()
        
    auctioneer_node = auction_req.auctioneer_node
    nodes_collected = rospy.get_param('~neighbour_nodes_list')
    auction_data = auction_req.auction_data



    # Create a bid messsage to put an offer for the item in auction_req!    
    bid = auction_msgs.msg.Bid()
    bid.header.frame_id = 'base_link' # to be rechecked
    bid.header.stamp = rospy.Time.now()
    bid.buyer_id = rospy.get_name()          
        
    if auction_req.auction_data.metrics == "distance":
        # to be given by the cost to go to position of the ocurring event
        # the cost for the metrics==distance is calculated using the euclidean
        # distance between the parameter position of the node and the task_position
        # given in the auction_req
        node_position = eval(rospy.get_param('~position'))
        x = float(node_position[0])-auction_req.auction_data.task_location.x
        y = float(node_position[1])-auction_req.auction_data.task_location.y
        z = float(node_position[2])-auction_req.auction_data.task_location.z
        bid.cost_distance = float(math.sqrt(x*x+y*y+z*z))
    else:
        rospy.loginfo("Metrics unkown")
        bid.cost_distance = 999999;

    # put bid to auctioneer
    service_path = auction_req.auctioneer_node+'/auctioneer_bid_reception_server'   
    
    rospy.wait_for_service(service_path)
    auctioneer_bid_reception_service = rospy.ServiceProxy(service_path, auction_srvs.srv.AuctioneerBidReceptionService)

    try:
        auctioneer_bid_reception_server_resp = auctioneer_bid_reception_service(sending_node,bid)

    except rospy.ServiceException, e:
        print "Service did not process request: %s"%str(e)



    # Relay information to neighbour nodes!
    neighbour_nodes_relay_list = auction_common.create_neighbour_nodes_list(auction_req)
           
    if neighbour_nodes_relay_list:
        
        for node in neighbour_nodes_relay_list:                  
            
            # prepare neighbours to be buyers
            service_path = node+'/auction_config_server'
            
            rospy.wait_for_service(service_path)
            neighbour_node_auction_config_server = rospy.ServiceProxy(service_path,
                                                                      auction_srvs.srv.AuctionConfigService)
            
            try:       
                neighbour_node_auction_config_server_resp = neighbour_node_auction_config_server(role,auction_type,sending_node)
                
            except rospy.ServiceException, e:
                rospy.loginfo("Service call failed: %s",e)
                
                
            # send the auction information to the buyer node
            service_path = node+'/buyer_server'   
                
            rospy.wait_for_service(service_path)
            buyer_service = rospy.ServiceProxy(service_path, auction_srvs.srv.BuyerService)
            
            try:
                buyer_server_resp = buyer_service(auctioneer_node,sending_node,nodes_collected,auction_data)
                
            except rospy.ServiceException, e:
                print "Service did not process request: %s"%str(e)    
    
                

    # return best bid
    return {'response_info': 'valid'+rospy.get_name()}
