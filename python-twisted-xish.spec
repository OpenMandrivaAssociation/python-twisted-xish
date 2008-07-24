Summary:        A XML API for Twisted framework
Name:           python-twisted-xish
Version: 0.1.0
%define directory_down %(echo %version|perl -n -e  '/^(\d+\.\d+).*$/; print \$1 ')
Release: %mkrel 7
Source0:        http://tmrc.mit.edu/mirror/twisted/Xish//%directory_down/TwistedXish-%{version}.tar.bz2
Source1:        _version.py
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/xish/
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel 
BuildRequires:  python-twisted-core
Requires:       python-twisted-core
#BuildArch:      noarch

%description
A XML API for Twisted framework.

%prep
%setup -q -n TwistedXish-%version
cp %SOURCE1 twisted/xish/

%build
%__python setup.py build

%install
%__rm -rf %buildroot
%__python setup.py install --root  %buildroot --install-purelib=%py_platsitedir

%clean
%__rm -rf %buildroot

%files
%defattr(0644,root,root,0755)
%doc LICENSE README 
%py_platsitedir/twisted/xish/
%py_platsitedir/*.egg-info


