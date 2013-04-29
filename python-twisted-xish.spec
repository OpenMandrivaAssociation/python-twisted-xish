Summary:        A XML API for Twisted framework
Name:           python-twisted-xish
Version: 0.1.0
%define directory_down %(echo %version|perl -n -e  '/^(\d+\.\d+).*$/; print \$1 ')
Release:        11
Source0:        http://tmrc.mit.edu/mirror/twisted/Xish//%directory_down/TwistedXish-%{version}.tar.bz2
Source1:        _version.py
License:        MIT
Group:          Development/Python
URL:            http://twistedmatrix.com/projects/xish/
BuildRequires:	python-devel 
BuildRequires:  python-twisted-core
Requires:       python-twisted-core
#BuildArch:      noarch

%define debug_package %{nil}

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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.0-10mdv2010.0
+ Revision: 442520
- rebuild

* Mon Dec 29 2008 Crispin Boylan <crisb@mandriva.org> 0.1.0-9mdv2009.1
+ Revision: 321219
- Rebuild for python2.6

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-8mdv2009.0
+ Revision: 259856
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.1.0-7mdv2009.0
+ Revision: 247703
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Dec 29 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.0-5mdv2008.1
+ Revision: 139217
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Dec 14 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.0-4mdv2007.0
+ Revision: 96934
- Rebuild against new python

  + Michael Scherer <misc@mandriva.org>
    - Import python-twisted-xish

* Fri Aug 11 2006 Michael Scherer <misc@mandriva.org> 0.1.0-3mdv2007.0
- rebuild for new tag
- add version .py for new twisted

* Wed Jan 25 2006 Michael Scherer <misc@mandriva.org> 0.1.0-2mdk
- make it rpmbuildupdatable
- make it arch dependant like other twisted package
- use macro

* Sun May 15 2005 Michael Scherer <misc@mandriva.org> 0.1.0-1mdk
- Initial package

