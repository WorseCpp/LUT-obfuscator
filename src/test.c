

    int f(int x)
    {
        return x * x * x * x;
    }

    int main() {
        int a = 0;
        int j = 0;
        int i = 0;
        if (a < 10) {
            a = a + 1;
        } else {
            a = a - 1;
            j -= 1;
        }
        while (a < 15) {
            a++;
            i += f(a);
        }
        return a;
    }
    