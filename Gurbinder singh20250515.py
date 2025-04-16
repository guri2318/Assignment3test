def requisition_approval():
   requisitiondata=requisitions_total()
   total=requisitiondata['total']

   if total < 500:
      status="approved"
   else:
      status="pending"

   print(f"status:{status}")


requisition_approval()
 


def display_requisitions(requisition):
    
    print("Printing Requisitions:\n")
    print(f"date:{requisition['requisition_id']}")
    print("staff_id")(requisition["requisition_id"])
    print(f'staff name:requisition[staff mame')
    print(f"total:$requisition[total']")
    print(f"stauts:reqisition['status']")


display_requisitions()
        
   