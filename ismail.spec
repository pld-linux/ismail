Summary:	Inside Systems webmail package
Summary(pl):	Webmail firmy Inside Systems
Name:		ismail
Version:	2.0
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.insidesystems.net/ismail/%{name}-%{version}.tar.bz2
# Source0-md5:	df7b88426f24250cd7ffee6f29d330b2
Source1:	%{name}.conf
URL:		http://www.insidesystems.net/projects/project.php?projectid=4
Requires:	php
Requires:	php-pcre
Requires:	php-imap
Requires:	php4-domxml
Requires:	webserver
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ismaildir	%{_datadir}/%{name}
%define 	_sysconfdir     /etc/%{name}

%description
This package contains ISMail, a webmail system for modern browsers.

%description -l pl
Ten pakiet zawiera ISMaila - system webmailowy dla nowoczesnych
przegl±darek.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ismaildir} \
	    $RPM_BUILD_ROOT{%{_sysconfdir},/etc/httpd}
mv ismail/include/ismail.conf.sample ismail/include/ismail.conf
mv ismail/include/istheme.conf.sample ismail/include/istheme.conf

cp -av ismail/* $RPM_BUILD_ROOT%{_ismaildir}

cp ismail/include/*.conf $RPM_BUILD_ROOT%{_sysconfdir}

ln -sf %{_sysconfdir}/ismail.conf               $RPM_BUILD_ROOT%{_ismaildir}/include/ismail.conf
ln -sf %{_sysconfdir}/istheme.conf               $RPM_BUILD_ROOT%{_ismaildir}/include/istheme.conf

install %{SOURCE1} $RPM_BUILD_ROOT/etc/httpd/%{name}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BSD CHANGELOG CREDITS docs.html examples
%dir %{_sysconfdir}
%{_sysconfdir}/*.conf
%dir %{_ismaildir}
%dir %{_ismaildir}/include
%config(noreplace) %verify(not md5 mtime size) %{_ismaildir}/include/*.conf
%{_ismaildir}/include/*.php
#%{_ismaildir}/include/*.class
%{_ismaildir}/include/*.xml
%dir %{_ismaildir}/include/datastores
%{_ismaildir}/include/datastores/*.php*
%{_ismaildir}/*.php
%{_ismaildir}/xtree
%{_ismaildir}/locale
%{_ismaildir}/themes
#%{_ismaildir}/graphics
#%attr(730,root,http) %dir %{_ismaildir}/users
%attr(640,root,root) /etc/httpd/%{name}.conf
