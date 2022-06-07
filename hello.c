#include "config.h"

#ifdef HAVE_STDIO_H
#include <stdio.h>


int print_hello()
{
    printf("Test task in RAIDIX!\n");
    return 0;
}
#else
#error stdio.h is needed for compilation
#endif

