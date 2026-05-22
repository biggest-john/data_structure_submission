package arrays.highArray;

public class HighArray {
    private long[] a;
    private int nElems;

    public HighArray(int max){
        a = new long[max];
        nElems = 0;
    }

    public boolean find(long searchKey){
        int j;
        for(j=0; j<nElems; j++)
            if(a[j] == searchKey)
                break;
        if(j == nElems)
            return false;
        return true;
    }

    public void insert(long value){
        a[nElems] = value;
        nElems++;
    }

    public void insert(int position, long value){
        for(int k = nElems+1; k>=position; k--){
            a[k] = a[k-1];
        }
        a[position] = value;
        nElems++;
    }

    public boolean delete(long value){
        int j;
        for(j=0; j<nElems; j++)
            if (value == a[j])
                break;
        if(j==nElems)
            return false;
        else {
            for(int k = j; k < nElems - 1; k++){
                a[k] = a[k+1];
            }
            nElems--;
        }
        return true;
    }

    public void display(){
        for (int j=0; j<nElems; j++)
            System.out.println(a[j] + " ");
        System.out.println("");
    }
}
