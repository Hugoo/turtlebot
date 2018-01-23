
(cl:in-package :asdf)

(defsystem "cam_tracker-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ChangeTrackingMode" :depends-on ("_package_ChangeTrackingMode"))
    (:file "_package_ChangeTrackingMode" :depends-on ("_package"))
  ))