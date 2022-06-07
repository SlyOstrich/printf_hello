Name:           RAIDIX_print
Version:        1.0
Release:        1%{?dist}
Summary:        A sample package, saying hello, RAIDIX
License:        GPL
URL:            https://github.com/SlyOstrich/printf_hello
Source0:        %{name}-%{version}.tar.gz

%define     _build_id_links none

%description
This package basically does nothing, but it potentially could do something useful.

%prep
%{__rm} -rf %{name}-%{version}
%{__mkdir} -p %{name}-%{version}
%{__tar} -xzvf %{SOURCE0} -C %{_builddir}/%{name}-%{version} --strip-components 1

%build
cd %{name}-%{version}
autoreconf
./configure
%{__make} all

%install
cd %{name}-%{version}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf $RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_DIR/*

%files
%defattr(-,root,root)
%{_usr}/lib64/libhello.so
%{_usr}/include/hello.h
%{_usr}/bin/print_hello


%changelog
* Tue Jun  7 2022 root
-
