
(cl:in-package :asdf)

(defsystem "axis_camera-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Axis" :depends-on ("_package_Axis"))
    (:file "_package_Axis" :depends-on ("_package"))
  ))