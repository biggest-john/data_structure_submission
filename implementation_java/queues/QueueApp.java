package queues;

public class QueueApp {
    public static void main(String[] args) {
        QueueClass newQueue = new QueueClass(5);

        //insert new items
        newQueue.insert(10); //0
        newQueue.insert(20); //1
        newQueue.insert(30); //2
        newQueue.insert(40); //3

        //remove new items
        System.out.println(newQueue.remove()); //0
        System.out.println(newQueue.remove()); //1
        System.out.println(newQueue.remove()); //2

        //testing the circular queue
        newQueue.insert(50); //4
        newQueue.insert(60); //5
        newQueue.insert(70); //0
        newQueue.insert(80); //1

        while (!newQueue.isEmpty()){
            System.out.print(newQueue.remove() + ", ");
        }
    }
}
