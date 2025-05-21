#include <stdio.h>

int mf_0(int pm_0) {
    if (pm_0 <= 0) {
        return pm_0 + 5;
    }
    int temp_val = (pm_0 * 1) - (pm_0 / 4);
    return mf_0(pm_0 - 1) + (temp_val % 7);
}


int f_0(int p_0) {
    int drv_0 = mf_0(5);
    int drv_1 = mf_0(5);
    if (p_0 <= 1)
    {
        int dead_v_0 = 9974;
        return 1;
    }
    else     {
        int dead_v_1 = 3379;
        return p_0 * f_0(p_0 + (0 - (1)));
    }
}

int main() {
    int v_0 = 6;
    int v_1 = f_0(v_0);
    int st_0 = 1;
    int dead_v_2 = 5224;
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