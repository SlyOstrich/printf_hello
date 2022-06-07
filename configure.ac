AC_INIT([hello], [0.0.1], [])
AC_PROG_CC
AH_TEMPLATE([HAVE_STDIO_H], [Definition of macros for existing of stdio.h])
AC_CHECK_HEADER([stdio.h],
                [AC_DEFINE([HAVE_STDIO_H], [1],
                    [Define to 1 if you have <stdio.h>.])],
                [AC_MSG_ERROR([Sorry, can't do anything for you])]
)
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_FILES([Makefile])
AC_OUTPUT
