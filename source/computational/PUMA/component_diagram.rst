.. uml::

   !define DIAG_NAME Component Diagram

   !include includes/skins.iuml

   skinparam backgroundColor #FFFFFF
   skinparam componentStyle uml2

   folder "PUMA" [[../computational/puma/index.html]] {
  
  [component #1]
  [component #2]
  [component #3]

  [component #1] -- [component #2]
}
