; Auto-generated. Do not edit!


(cl:in-package race-msg)


;//! \htmlinclude velocity_param.msg.html

(cl:defclass <velocity_param> (roslisp-msg-protocol:ros-message)
  ((velocity
    :reader velocity
    :initarg :velocity
    :type cl:float
    :initform 0.0))
)

(cl:defclass velocity_param (<velocity_param>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <velocity_param>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'velocity_param)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name race-msg:<velocity_param> is deprecated: use race-msg:velocity_param instead.")))

(cl:ensure-generic-function 'velocity-val :lambda-list '(m))
(cl:defmethod velocity-val ((m <velocity_param>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader race-msg:velocity-val is deprecated.  Use race-msg:velocity instead.")
  (velocity m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <velocity_param>) ostream)
  "Serializes a message object of type '<velocity_param>"
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'velocity))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <velocity_param>) istream)
  "Deserializes a message object of type '<velocity_param>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'velocity) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<velocity_param>)))
  "Returns string type for a message object of type '<velocity_param>"
  "race/velocity_param")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'velocity_param)))
  "Returns string type for a message object of type 'velocity_param"
  "race/velocity_param")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<velocity_param>)))
  "Returns md5sum for a message object of type '<velocity_param>"
  "e4ff88b32504f688719a85e0753f63ce")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'velocity_param)))
  "Returns md5sum for a message object of type 'velocity_param"
  "e4ff88b32504f688719a85e0753f63ce")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<velocity_param>)))
  "Returns full string definition for message of type '<velocity_param>"
  (cl:format cl:nil "float32 velocity~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'velocity_param)))
  "Returns full string definition for message of type 'velocity_param"
  (cl:format cl:nil "float32 velocity~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <velocity_param>))
  (cl:+ 0
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <velocity_param>))
  "Converts a ROS message object to a list"
  (cl:list 'velocity_param
    (cl:cons ':velocity (velocity msg))
))
