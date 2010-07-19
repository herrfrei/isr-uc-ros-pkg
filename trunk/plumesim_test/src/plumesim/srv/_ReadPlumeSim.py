# autogenerated by genmsg_py from ReadPlumeSimRequest.msg. Do not edit.
import roslib.message
import struct

import geometry_msgs.msg
import nav_msgs.msg
import roslib.msg

class ReadPlumeSimRequest(roslib.message.Message):
  _md5sum = "75d9701e058ed9a7608ba3dbc16b5b7e"
  _type = "plumesim/ReadPlumeSimRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """nav_msgs/Odometry odom

================================================================================
MSG: nav_msgs/Odometry
# This represents an estimate of a position and velocity in free space.  
# The pose in this message should be specified in the coordinate frame given by header.frame_id.
# The twist in this message should be specified in the coordinate frame given by the child_frame_id
Header header
string child_frame_id
geometry_msgs/PoseWithCovariance pose
geometry_msgs/TwistWithCovariance twist

================================================================================
MSG: roslib/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/PoseWithCovariance
# This represents a pose in free space with uncertainty.

Pose pose

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of postion and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: geometry_msgs/TwistWithCovariance
# This expresses velocity in free space with uncertianty.

Twist twist

# Row-major representation of the 6x6 covariance matrix
# The orientation parameters use a fixed-axis representation.
# In order, the parameters are:
# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)
float64[36] covariance

================================================================================
MSG: geometry_msgs/Twist
# This expresses velocity in free space broken into it's linear and angular parts. 
Vector3  linear
Vector3  angular

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 

float64 x
float64 y
float64 z
"""
  __slots__ = ['odom']
  _slot_types = ['nav_msgs/Odometry']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   odom
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(ReadPlumeSimRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.odom is None:
        self.odom = nav_msgs.msg.Odometry()
    else:
      self.odom = nav_msgs.msg.Odometry()

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<3I', self.odom.header.seq, self.odom.header.stamp.secs, self.odom.header.stamp.nsecs))
      length = len(self.odom.header.frame_id)
      #serialize self.odom.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.odom.header.frame_id))
      length = len(self.odom.child_frame_id)
      #serialize self.odom.child_frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.odom.child_frame_id))
      buff.write(struct.pack('<7d', self.odom.pose.pose.position.x, self.odom.pose.pose.position.y, self.odom.pose.pose.position.z, self.odom.pose.pose.orientation.x, self.odom.pose.pose.orientation.y, self.odom.pose.pose.orientation.z, self.odom.pose.pose.orientation.w))
      #serialize self.odom.pose.covariance
      buff.write(struct.pack('<36d', *self.odom.pose.covariance))
      buff.write(struct.pack('<6d', self.odom.twist.twist.linear.x, self.odom.twist.twist.linear.y, self.odom.twist.twist.linear.z, self.odom.twist.twist.angular.x, self.odom.twist.twist.angular.y, self.odom.twist.twist.angular.z))
      #serialize self.odom.twist.covariance
      buff.write(struct.pack('<36d', *self.odom.twist.covariance))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      if self.odom is None:
        self.odom = nav_msgs.msg.Odometry()
      end = 0
      start = end
      end += 12
      (self.odom.header.seq, self.odom.header.stamp.secs, self.odom.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.odom.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.odom.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.odom.child_frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.odom.child_frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 56
      (self.odom.pose.pose.position.x, self.odom.pose.pose.position.y, self.odom.pose.pose.position.z, self.odom.pose.pose.orientation.x, self.odom.pose.pose.orientation.y, self.odom.pose.pose.orientation.z, self.odom.pose.pose.orientation.w,) = struct.unpack('<7d',str[start:end])
      #deserialize self.odom.pose.covariance
      start = end
      end += 288
      self.odom.pose.covariance = struct.unpack('<36d',str[start:end])
      start = end
      end += 48
      (self.odom.twist.twist.linear.x, self.odom.twist.twist.linear.y, self.odom.twist.twist.linear.z, self.odom.twist.twist.angular.x, self.odom.twist.twist.angular.y, self.odom.twist.twist.angular.z,) = struct.unpack('<6d',str[start:end])
      #deserialize self.odom.twist.covariance
      start = end
      end += 288
      self.odom.twist.covariance = struct.unpack('<36d',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<3I', self.odom.header.seq, self.odom.header.stamp.secs, self.odom.header.stamp.nsecs))
      length = len(self.odom.header.frame_id)
      #serialize self.odom.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.odom.header.frame_id))
      length = len(self.odom.child_frame_id)
      #serialize self.odom.child_frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.odom.child_frame_id))
      buff.write(struct.pack('<7d', self.odom.pose.pose.position.x, self.odom.pose.pose.position.y, self.odom.pose.pose.position.z, self.odom.pose.pose.orientation.x, self.odom.pose.pose.orientation.y, self.odom.pose.pose.orientation.z, self.odom.pose.pose.orientation.w))
      #serialize self.odom.pose.covariance
      buff.write(self.odom.pose.covariance.tostring())
      buff.write(struct.pack('<6d', self.odom.twist.twist.linear.x, self.odom.twist.twist.linear.y, self.odom.twist.twist.linear.z, self.odom.twist.twist.angular.x, self.odom.twist.twist.angular.y, self.odom.twist.twist.angular.z))
      #serialize self.odom.twist.covariance
      buff.write(self.odom.twist.covariance.tostring())
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      if self.odom is None:
        self.odom = nav_msgs.msg.Odometry()
      end = 0
      start = end
      end += 12
      (self.odom.header.seq, self.odom.header.stamp.secs, self.odom.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.odom.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.odom.header.frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.odom.child_frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.odom.child_frame_id,) = struct.unpack(pattern, str[start:end])
      start = end
      end += 56
      (self.odom.pose.pose.position.x, self.odom.pose.pose.position.y, self.odom.pose.pose.position.z, self.odom.pose.pose.orientation.x, self.odom.pose.pose.orientation.y, self.odom.pose.pose.orientation.z, self.odom.pose.pose.orientation.w,) = struct.unpack('<7d',str[start:end])
      #deserialize self.odom.pose.covariance
      start = end
      end += 288
      self.odom.pose.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      start = end
      end += 48
      (self.odom.twist.twist.linear.x, self.odom.twist.twist.linear.y, self.odom.twist.twist.linear.z, self.odom.twist.twist.angular.x, self.odom.twist.twist.angular.y, self.odom.twist.twist.angular.z,) = struct.unpack('<6d',str[start:end])
      #deserialize self.odom.twist.covariance
      start = end
      end += 288
      self.odom.twist.covariance = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=36)
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

# autogenerated by genmsg_py from ReadPlumeSimResponse.msg. Do not edit.
import roslib.message
import struct

import roslib.msg
import plumesim.msg

class ReadPlumeSimResponse(roslib.message.Message):
  _md5sum = "ede17dfddda6f65ef9598907b1bddb2a"
  _type = "plumesim/ReadPlumeSimResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """NoseSniff sniff


================================================================================
MSG: plumesim/NoseSniff
Header header
string[] sensor_model
float32[] reading
float32 temperature_c	# temperature in celsius
float32 temperature_f	# temperature in fahrenheit
float32 humidity	# humidity in %


================================================================================
MSG: roslib/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.secs: seconds (stamp_secs) since epoch
# * stamp.nsecs: nanoseconds since stamp_secs
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

"""
  __slots__ = ['sniff']
  _slot_types = ['plumesim/NoseSniff']

  ## Constructor. Any message fields that are implicitly/explicitly
  ## set to None will be assigned a default value. The recommend
  ## use is keyword arguments as this is more robust to future message
  ## changes.  You cannot mix in-order arguments and keyword arguments.
  ##
  ## The available fields are:
  ##   sniff
  ##
  ## @param self: self
  ## @param args: complete set of field values, in .msg order
  ## @param kwds: use keyword arguments corresponding to message field names
  ## to set specific fields. 
  def __init__(self, *args, **kwds):
    if args or kwds:
      super(ReadPlumeSimResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.sniff is None:
        self.sniff = plumesim.msg.NoseSniff()
    else:
      self.sniff = plumesim.msg.NoseSniff()

  ## internal API method
  def _get_types(self): return self._slot_types

  ## serialize message into buffer
  ## @param buff StringIO: buffer
  def serialize(self, buff):
    try:
      buff.write(struct.pack('<3I', self.sniff.header.seq, self.sniff.header.stamp.secs, self.sniff.header.stamp.nsecs))
      length = len(self.sniff.header.frame_id)
      #serialize self.sniff.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.sniff.header.frame_id))
      #serialize self.sniff.sensor_model
      length = len(self.sniff.sensor_model)
      buff.write(struct.pack('<I', length))
      for val1 in self.sniff.sensor_model:
        length = len(val1)
        #serialize val1
        buff.write(struct.pack('<I%ss'%length, length, val1))
      #serialize self.sniff.reading
      length = len(self.sniff.reading)
      buff.write(struct.pack('<I', length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.sniff.reading))
      buff.write(struct.pack('<3f', self.sniff.temperature_c, self.sniff.temperature_f, self.sniff.humidity))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance
  ## @param self: self
  ## @param str str: byte array of serialized message
  def deserialize(self, str):
    try:
      if self.sniff is None:
        self.sniff = plumesim.msg.NoseSniff()
      end = 0
      start = end
      end += 12
      (self.sniff.header.seq, self.sniff.header.stamp.secs, self.sniff.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.sniff.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.sniff.header.frame_id,) = struct.unpack(pattern, str[start:end])
      #deserialize self.sniff.sensor_model
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.sniff.sensor_model = []
      for i in xrange(0, length):
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1,) = struct.unpack(pattern, str[start:end])
        self.sniff.sensor_model.append(val1)
      #deserialize self.sniff.reading
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.sniff.reading = struct.unpack(pattern, str[start:end])
      start = end
      end += 12
      (self.sniff.temperature_c, self.sniff.temperature_f, self.sniff.humidity,) = struct.unpack('<3f',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill


  ## serialize message with numpy array types into buffer
  ## @param self: self
  ## @param buff StringIO: buffer
  ## @param numpy module: numpy python module
  def serialize_numpy(self, buff, numpy):
    try:
      buff.write(struct.pack('<3I', self.sniff.header.seq, self.sniff.header.stamp.secs, self.sniff.header.stamp.nsecs))
      length = len(self.sniff.header.frame_id)
      #serialize self.sniff.header.frame_id
      buff.write(struct.pack('<I%ss'%length, length, self.sniff.header.frame_id))
      #serialize self.sniff.sensor_model
      length = len(self.sniff.sensor_model)
      buff.write(struct.pack('<I', length))
      for val1 in self.sniff.sensor_model:
        length = len(val1)
        #serialize val1
        buff.write(struct.pack('<I%ss'%length, length, val1))
      #serialize self.sniff.reading
      length = len(self.sniff.reading)
      buff.write(struct.pack('<I', length))
      pattern = '<%sf'%length
      buff.write(self.sniff.reading.tostring())
      buff.write(struct.pack('<3f', self.sniff.temperature_c, self.sniff.temperature_f, self.sniff.humidity))
    except struct.error, se: self._check_types(se)
    except TypeError, te: self._check_types(te)

  ## unpack serialized message in str into this message instance using numpy for array types
  ## @param self: self
  ## @param str str: byte array of serialized message
  ## @param numpy module: numpy python module
  def deserialize_numpy(self, str, numpy):
    try:
      if self.sniff is None:
        self.sniff = plumesim.msg.NoseSniff()
      end = 0
      start = end
      end += 12
      (self.sniff.header.seq, self.sniff.header.stamp.secs, self.sniff.header.stamp.nsecs,) = struct.unpack('<3I',str[start:end])
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      #deserialize self.sniff.header.frame_id
      pattern = '<%ss'%length
      start = end
      end += struct.calcsize(pattern)
      (self.sniff.header.frame_id,) = struct.unpack(pattern, str[start:end])
      #deserialize self.sniff.sensor_model
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      self.sniff.sensor_model = []
      for i in xrange(0, length):
        start = end
        end += 4
        (length,) = struct.unpack('<I',str[start:end])
        #deserialize val1
        pattern = '<%ss'%length
        start = end
        end += struct.calcsize(pattern)
        (val1,) = struct.unpack(pattern, str[start:end])
        self.sniff.sensor_model.append(val1)
      #deserialize self.sniff.reading
      start = end
      end += 4
      (length,) = struct.unpack('<I',str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.sniff.reading = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 12
      (self.sniff.temperature_c, self.sniff.temperature_f, self.sniff.humidity,) = struct.unpack('<3f',str[start:end])
      return self
    except struct.error, e:
      raise roslib.message.DeserializationError(e) #most likely buffer underfill

class ReadPlumeSim(roslib.message.ServiceDefinition):
  _type          = 'plumesim/ReadPlumeSim'
  _md5sum = 'd189ef261c3d25d1f5ebde5203c19982'
  _request_class  = ReadPlumeSimRequest
  _response_class = ReadPlumeSimResponse