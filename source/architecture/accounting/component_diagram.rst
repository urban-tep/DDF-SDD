.. uml::
  :caption: Accounting component diagram
  :align: center


  !include includes/skins.iuml

  skinparam backgroundColor #FFFFFF
  skinparam componentStyle uml2

  !include source/groups/group___apel_accounting.iuml

  !include source/groups/group___apel.iuml

  folder "Accounting" {
      database "Accounting Storage" as AAS [[../../architecture/accounting/accounting.html]]
      group___apel_server -down- AAS
  }


