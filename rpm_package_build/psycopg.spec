%define name psycopg
%define version 3.1.12 
%define unmangled_version 3.1.12 
%define release 1

Summary: Python example psycopg package
Name: %{name}
Version: %{version}
Release: %{release}
Source0: https://files.pythonhosted.org/packages/42/30/73ebc6d40269fa4fdc090c374d1dd30df822e885a742719b0fe952c9d86c/psycopg-3.1.12.tar.gz
License: Apache License 2.0
Group: Development/Libraries

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Dmitriy Konichev <dima@example.com>

%description
psycopg in RPM package 

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version}

%build
python3 setup.py build

%install
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)