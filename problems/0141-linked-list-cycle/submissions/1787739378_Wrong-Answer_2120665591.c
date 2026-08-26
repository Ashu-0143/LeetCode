bool hasCycle(struct ListNode *head) {
    if (head==NULL) return 0;
    struct ListNode *slow=head->next;
    struct ListNode *fast=head;
    while(slow!=NULL)
    {
        if (slow->next==NULL||fast->next==NULL||fast->next->next==NULL)
        return 0;
        if(slow==fast){
        return 1;}
        slow=slow->next;
        fast=fast->next->next;
    }
    return 0;
}
