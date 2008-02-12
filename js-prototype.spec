Summary:	Prototype JavaScript framework: Easy Ajax and DOM manipulation for dynamic web application.
Name:		prototype
Version:	1.6.0.2
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	http://www.prototypejs.org/assets/2008/1/25/prototype-1.6.0.2.js
# Source0-md5:	d3a5b20d5368c1bcabe655b57b52d097
URL:		http://www.prototypejs.org/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Prototype is a JavaScript Framework that aims to ease development of dynamic
web applications.

Featuring a unique, easy-to-use toolkit for class-driven development and the
nicest Ajax library around, Prototype is quickly becoming the codebase of
choice for web application developers everywhere.

%prep
%setup -qcT
cp -a %{SOURCE0} %{name}.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -a %{name}.js $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_appdir}
