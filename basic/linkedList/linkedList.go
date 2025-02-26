package main
import (
	"fmt"
)

type ListNode struct {
	Val int
	Next *ListNode
}


func createLinkedList(arr []int) *ListNode {
	if arr == nil || len(arr) == 0 {
		return nil
	}

	head := &ListNode{Val: arr[0]}
	cur := head
	for i := 1; i < len(arr); i++ {
		cur.Next = &ListNode{Val: arr[i]}
		cur = cur.Next
	}
	return head
}


func main() {
	head := createLinkedList([]int{1, 2, 3, 4, 5, 6})
	newHead := &ListNode{Val: 10}
	newHead.Next = head
	head = newHead
	newTail := &ListNode{Val: 20}
	cur := head
	for cur.Next != nil {
		cur = cur.Next
	}
	cur.Next = newTail

	for p := head; p != nil; p = p.Next {
		fmt.Println(p.Val)
	}

}
