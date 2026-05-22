package stacks;

public class StackApp {
    public static void main(String[] args) {
        StackX newStack = new StackX(50);

        newStack.push(20);
        newStack.push(40);
        newStack.push(60);
        newStack.push(80);

        //displaying the items in the stack
        while(!newStack.isEmpty()){
            System.out.print(newStack.pop() + ", ");
        }
        //observe how the last element added to the stack
        //is the first to be printed out
    }
}
