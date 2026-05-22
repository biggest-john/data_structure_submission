package arrays;

public class Arrays {
    public static void main(String[] args) {
        long[] arr;
        arr = new long[100];
        int nElems = 0;
        int j;
        long searchKey;

        arr[0] = 77;
        arr[1] = 99;
        arr[2] = 44;
        arr[3] = 55;
        arr[4] = 22;
        arr[5] = 88;
        arr[6] = 11;
        arr[7] = 00;
        arr[8] = 66;
        arr[9] = 10;

        nElems = 10; // number of elements in the array

        System.out.println("Before Operation");
        for(j = 0; j < nElems; j++)
            System.out.println(arr[j] + " ");
        System.out.println("");

        //searching an element
        searchKey = 66;
        for(j = 0; j < nElems; j++)
            if(arr[j] == searchKey)
                break;

        if(j == nElems)
            System.out.println("Can't find " + searchKey);
        else
            System.out.println("Found " + searchKey);

        //deleting an element
        searchKey = 55; //element to delete
        for(j = 0; j<nElems; j++)
            if(arr[j] == searchKey)
                break;
        for(int k=j; k<nElems-1; j++){
            arr[k] = arr[k+1];
        }
        nElems--;

        //display elements
        System.out.println("After deletion");
        for(j=0; j<nElems; j++)
            System.out.println(arr[j] + " ");
        System.out.println("");
    }
}
