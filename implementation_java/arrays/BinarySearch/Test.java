package arrays.BinarySearch;

public class Test {
    static long[] a;
    static int nElems = 0;
    public static void main(String[] args) {
        a = new long[100];
        int j;
        long searchKey;

        a[0] = 77;
        a[1] = 99;
        a[2] = 44;
        a[3] = 55;
        a[4] = 22;
        a[5] = 88;
        a[6] = 11;
        a[7] = 00;
        a[8] = 66;
        a[9] = 10;

        nElems = 10; // number of elements in the array
    }
    public int find(long searchKey){
        int lowerBound = 0;
        int upperBound = nElems - 1;

        int curIn;

        while(true){
            curIn = (lowerBound + upperBound) / 2;

            if(a[curIn] == searchKey)
                return curIn;
            else if(lowerBound > upperBound)
                return nElems;
            else{
                if(a[curIn] < searchKey)
                    lowerBound = curIn + 1; //it's in upper half
                else
                    upperBound = curIn - 1;
            }
        }
    }
}
