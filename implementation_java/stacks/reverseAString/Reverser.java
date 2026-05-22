package stacks.reverseAString;

public class Reverser {
    private String input;
    private String output;

    public Reverser(String in){
        input = in;
    }

    public String doRev(){
        int stackSize = input.length();
        StackX revStack = new StackX(stackSize);

        for(int j = 0; j < input.length(); j++){
            char ch = input.charAt(j);
            revStack.push(ch);
        }

        output = "";
        while (!revStack.isEmpty()){
            char ch = revStack.pop();
            output = output + ch;
        }

        return output;
    }
}
