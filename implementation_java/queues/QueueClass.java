package queues;

public class QueueClass {
    private int maxSize;
    private long[] queueArray;
    private int front;
    private int rear;
    private int nItems;

    public QueueClass(int s){
        maxSize = s;
        queueArray = new long[maxSize];
        front = 0;  //used to fetch elements from the front
        rear = -1;  //used to add elements at the back
        nItems = 0; //counts the number of elements in the queue
    }

    public void insert(long j){
        //check if queue is full before insertion
        if(isFull())
            throw new RuntimeException("Queue is full");

        //check if stack is full and add new elements to the front
        if(rear == maxSize - 1)
            rear = -1;

        queueArray[++rear] = j;
        nItems++;
    }

    public long remove(){
        if(isEmpty())
            throw new RuntimeException("Queue is empty!");

        long returnValue = queueArray[front++];

        //check if we have gotten to the end of the queue
        //then return the pointer to the front of the queue
        if(front == maxSize)
            front = 0;

        nItems--;
        return returnValue;
    }

    public long peekFront(){
        return queueArray[front];
    }

    public boolean isEmpty(){
        return (nItems == 0);
    }

    public boolean isFull(){
        return (nItems == maxSize);
    }

    public int size(){
        return nItems;
    }
}
