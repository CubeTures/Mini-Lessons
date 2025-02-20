# C Programming

-   Pointers rule everything
-   Pointer arithmetic
-   Struct padding and packing
-   Neither object oriented nor functional
-   Little endian
-   Function pointers
-   malloc, realloc, and free
-   Literally just system notes

```c
int main() {
    int *p = [1, 2, 3, 4, 5, 6]
    int a = *(int*)((char*)p + 8)
    cout << a << endl;
}
```
