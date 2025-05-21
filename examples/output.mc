#include <stdio.h>

int mf_0(int pm_0) {
    if (pm_0 <= 1) {
        return pm_0 + 4;
    }
    int temp_val = (pm_0 * 2) - (pm_0 / 5);
    return mf_0(pm_0 - 2) + (temp_val % 6);
}


int f_0(int p_0) {
    int dead_v_0 = 5743;
    if (p_0 <= 1)
    {
        int dead_v_1 = 1722;
        return 1;
    }
    else     {
        int dead_v_2 = 1718;
        return p_0 * f_0(p_0 + (0 - (1)));
    }
}

int main() {
    int v_0 = 6;
    int v_1 = f_0(v_0);
    int st_0 = 1;
    int dead_v_3 = 7723;
    while (st_0 > 0) {
        switch (st_0) {
        case 1:
            printf("%d", v_1);
            st_0 = 2;
            break;
        case 2:
            return 0;
            st_0 = 0;
            break;
        default:
            st_0 = 0;
            break;
    }
}
}