Summary:	Prototype JavaScript framework: Easy Ajax and DOM manipulation for dynamic web application
Name:		prototype
Version:	1.6.0.3
Release:	3
License:	MIT
Group:		Applications/WWW
Source0:	http://www.prototypejs.org/assets/2008/9/29/%{name}-%{version}.js
# Source0-md5:	b5684120e496c310977713be34be4868
URL:		http://www.prototypejs.org/
BuildRequires:	sed >= 4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_sysconfdir	%{_webapps}/%{_webapp}
%define		_appdir	%{_datadir}/%{name}

%description
Prototype is a JavaScript Framework that aims to ease development of
dynamic web applications.

Featuring a unique, easy-to-use toolkit for class-driven development
and the nicest Ajax library around, Prototype is quickly becoming the
codebase of choice for web application developers everywhere.

%prep
%setup -qcT
cp -a %{SOURCE0} %{name}.js

cat <<'EOF' > apache.conf
Alias /%{name}.js %{_appdir}/%{name}.js
Alias /js/%{name}.js %{_appdir}/%{name}.js
<Directory %{_appdir}>
	Allow from all
</Directory>
EOF

cat > lighttpd.conf <<'EOF'
alias.url += (
    "/%{name}.js/" => "%{_appdir}/%{name}.js",
    "/js/%{name}.js/" => "%{_appdir}/%{name}.js",
)
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdir},%{_sysconfdir}}
cp -a %{name}.js $RPM_BUILD_ROOT%{_appdir}

cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/apache.conf
cp -a apache.conf $RPM_BUILD_ROOT%{_sysconfdir}/httpd.conf
cp -a lighttpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/lighttpd.conf

%clean
rm -rf $RPM_BUILD_ROOT

%triggerin -- apache1 < 1.3.37-3, apache1-base
%webapp_register apache %{_webapp}

%triggerun -- apache1 < 1.3.37-3, apache1-base
%webapp_unregister apache %{_webapp}

%triggerin -- apache < 2.2.0, apache-base
%webapp_register httpd %{_webapp}

%triggerun -- apache < 2.2.0, apache-base
%webapp_unregister httpd %{_webapp}

%triggerin -- lighttpd
%webapp_register lighttpd %{_webapp}

%triggerun -- lighttpd
%webapp_unregister lighttpd %{_webapp}

%files
%defattr(644,root,root,755)
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/apache.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/httpd.conf
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lighttpd.conf
%{_appdir}
