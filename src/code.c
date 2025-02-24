

    int g(int x)
    {
        float i = 0;
        i = x * x;
        return i*8;
    }

    int f(int x)
    {
        return x * x * x * x;
    }

    int main() {

        int i = 0;
        int a = 0;
        int j = 0;
        j = f(10);
        if (a < 10) {
            a = a + 1;
        } else {
            a = a - 1;
        }
        while (a < 15) {
            a++;
            i += f(a);
        }
        return a;
    }
    