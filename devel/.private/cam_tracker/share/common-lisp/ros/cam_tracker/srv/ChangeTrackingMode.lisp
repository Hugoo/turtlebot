; Auto-generated. Do not edit!


(cl:in-package cam_tracker-srv)


;//! \htmlinclude ChangeTrackingMode-request.msg.html

(cl:defclass <ChangeTrackingMode-request> (roslisp-msg-protocol:ros-message)
  ((command
    :reader command
    :initarg :command
    :type cl:string
    :initform ""))
)

(cl:defclass ChangeTrackingMode-request (<ChangeTrackingMode-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeTrackingMode-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeTrackingMode-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cam_tracker-srv:<ChangeTrackingMode-request> is deprecated: use cam_tracker-srv:ChangeTrackingMode-request instead.")))

(cl:ensure-generic-function 'command-val :lambda-list '(m))
(cl:defmethod command-val ((m <ChangeTrackingMode-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader cam_tracker-srv:command-val is deprecated.  Use cam_tracker-srv:command instead.")
  (command m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeTrackingMode-request>) ostream)
  "Serializes a message object of type '<ChangeTrackingMode-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'command))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'command))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeTrackingMode-request>) istream)
  "Deserializes a message object of type '<ChangeTrackingMode-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'command) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'command) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeTrackingMode-request>)))
  "Returns string type for a service object of type '<ChangeTrackingMode-request>"
  "cam_tracker/ChangeTrackingModeRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeTrackingMode-request)))
  "Returns string type for a service object of type 'ChangeTrackingMode-request"
  "cam_tracker/ChangeTrackingModeRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeTrackingMode-request>)))
  "Returns md5sum for a message object of type '<ChangeTrackingMode-request>"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeTrackingMode-request)))
  "Returns md5sum for a message object of type 'ChangeTrackingMode-request"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeTrackingMode-request>)))
  "Returns full string definition for message of type '<ChangeTrackingMode-request>"
  (cl:format cl:nil "string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeTrackingMode-request)))
  "Returns full string definition for message of type 'ChangeTrackingMode-request"
  (cl:format cl:nil "string command~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeTrackingMode-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'command))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeTrackingMode-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeTrackingMode-request
    (cl:cons ':command (command msg))
))
;//! \htmlinclude ChangeTrackingMode-response.msg.html

(cl:defclass <ChangeTrackingMode-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass ChangeTrackingMode-response (<ChangeTrackingMode-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ChangeTrackingMode-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ChangeTrackingMode-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name cam_tracker-srv:<ChangeTrackingMode-response> is deprecated: use cam_tracker-srv:ChangeTrackingMode-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ChangeTrackingMode-response>) ostream)
  "Serializes a message object of type '<ChangeTrackingMode-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ChangeTrackingMode-response>) istream)
  "Deserializes a message object of type '<ChangeTrackingMode-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ChangeTrackingMode-response>)))
  "Returns string type for a service object of type '<ChangeTrackingMode-response>"
  "cam_tracker/ChangeTrackingModeResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeTrackingMode-response)))
  "Returns string type for a service object of type 'ChangeTrackingMode-response"
  "cam_tracker/ChangeTrackingModeResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ChangeTrackingMode-response>)))
  "Returns md5sum for a message object of type '<ChangeTrackingMode-response>"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ChangeTrackingMode-response)))
  "Returns md5sum for a message object of type 'ChangeTrackingMode-response"
  "cba5e21e920a3a2b7b375cb65b64cdea")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ChangeTrackingMode-response>)))
  "Returns full string definition for message of type '<ChangeTrackingMode-response>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ChangeTrackingMode-response)))
  "Returns full string definition for message of type 'ChangeTrackingMode-response"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ChangeTrackingMode-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ChangeTrackingMode-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ChangeTrackingMode-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ChangeTrackingMode)))
  'ChangeTrackingMode-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ChangeTrackingMode)))
  'ChangeTrackingMode-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ChangeTrackingMode)))
  "Returns string type for a service object of type '<ChangeTrackingMode>"
  "cam_tracker/ChangeTrackingMode")