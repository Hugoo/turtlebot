;; Auto-generated. Do not edit!


(when (boundp 'cam_tracker::ChangeTrackingMode)
  (if (not (find-package "CAM_TRACKER"))
    (make-package "CAM_TRACKER"))
  (shadow 'ChangeTrackingMode (find-package "CAM_TRACKER")))
(unless (find-package "CAM_TRACKER::CHANGETRACKINGMODE")
  (make-package "CAM_TRACKER::CHANGETRACKINGMODE"))
(unless (find-package "CAM_TRACKER::CHANGETRACKINGMODEREQUEST")
  (make-package "CAM_TRACKER::CHANGETRACKINGMODEREQUEST"))
(unless (find-package "CAM_TRACKER::CHANGETRACKINGMODERESPONSE")
  (make-package "CAM_TRACKER::CHANGETRACKINGMODERESPONSE"))

(in-package "ROS")





(defclass cam_tracker::ChangeTrackingModeRequest
  :super ros::object
  :slots (_command ))

(defmethod cam_tracker::ChangeTrackingModeRequest
  (:init
   (&key
    ((:command __command) "")
    )
   (send-super :init)
   (setq _command (string __command))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass cam_tracker::ChangeTrackingModeResponse
  :super ros::object
  :slots ())

(defmethod cam_tracker::ChangeTrackingModeResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass cam_tracker::ChangeTrackingMode
  :super ros::object
  :slots ())

(setf (get cam_tracker::ChangeTrackingMode :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get cam_tracker::ChangeTrackingMode :datatype-) "cam_tracker/ChangeTrackingMode")
(setf (get cam_tracker::ChangeTrackingMode :request) cam_tracker::ChangeTrackingModeRequest)
(setf (get cam_tracker::ChangeTrackingMode :response) cam_tracker::ChangeTrackingModeResponse)

(defmethod cam_tracker::ChangeTrackingModeRequest
  (:response () (instance cam_tracker::ChangeTrackingModeResponse :init)))

(setf (get cam_tracker::ChangeTrackingModeRequest :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get cam_tracker::ChangeTrackingModeRequest :datatype-) "cam_tracker/ChangeTrackingModeRequest")
(setf (get cam_tracker::ChangeTrackingModeRequest :definition-)
      "string command
---
")

(setf (get cam_tracker::ChangeTrackingModeResponse :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get cam_tracker::ChangeTrackingModeResponse :datatype-) "cam_tracker/ChangeTrackingModeResponse")
(setf (get cam_tracker::ChangeTrackingModeResponse :definition-)
      "string command
---
")



(provide :cam_tracker/ChangeTrackingMode "cba5e21e920a3a2b7b375cb65b64cdea")


