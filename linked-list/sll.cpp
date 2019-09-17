#include <iostream>
#include <algorithm>

using namespace std;

struct Node
{
    int data;
    Node *prev;
    Node *next;
};

class SLinkedList
{
public:
    Node *head, *tail;

    SLinkedList()
    {
        head = NULL;
        tail = NULL;
    }

    void display();
    void displayReverse(Node *);
    void createNodes(int);
    void insertStart(int);
    void insertEnd(int);
    void insertPos(int, int);
    void deleteStart();
    void deleteEnd();
    void deletePos(int);
    void reverseList();
    void insertionSort();

    int getLength();
};

void SLinkedList::createNodes(int n)
{
    int data;
    for (int i = 0; i < n; i++)
    {
        cout << "Enter data for node #" << i + 1 << ": ";
        cin >> data;

        Node *new_node = new Node;
        new_node->data = data;

        if (head == NULL && tail == NULL)
        {
            head = new_node;
        }
        else if (head == tail)
        {
            head->next = new_node;
        }
        else
        {
            tail->next = new_node;
        }

        tail = new_node;
    }
}

void SLinkedList::display()
{
    if (head == NULL)
    {
        cout << "List empty.\n";
        return;
    }

    Node *temp = head;

    while (temp != NULL)
    {
        cout << temp->data << " ";
        temp = temp->next;
    }
}

void SLinkedList::displayReverse(Node* head)
{
    if (head == NULL)
    {
        return;
    }
    
    displayReverse(head->next);
    cout << head->data << " ";
}

void SLinkedList::insertStart(int data)
{
    Node *new_node = new Node;
    new_node->data = data;
    
    if (head == NULL)
    {
        tail = new_node;
    }
    else
    {
        new_node->next = head;
    }

    head = new_node;
}

void SLinkedList::insertEnd(int data)
{
    Node *new_node = new Node;
    new_node->data = data;

    if (head == NULL)
    {
        head = new_node;
    }
    else
    {
        tail->next = new_node;
    }
    
    tail = new_node;
}

void SLinkedList::insertPos(int data, int pos)
{
    Node *new_node = new Node;
    new_node->data = data;

    if (head == NULL || pos == 0)
    {
        insertStart(data);
    }
    else
    {
        Node *temp = head;
        
        while (pos--)
        {
            temp = temp->next;
        }

        new_node->next = temp->next;
        temp->next = new_node;
    }
}

int main()
{
    SLinkedList sll;

    sll.createNodes(4);
    
    sll.display();
    cout << endl;
    


    return 0;
}