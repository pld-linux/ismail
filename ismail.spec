Summary:	Inside Systems webmail package
Name:		ISMail
Version:	1.7.1
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.verbotenplanet.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	3eb24555525da214e70b81292956867f
URL:		http://www.insidesystems.net/projects/project.php?projectid=4
Requires:	webserver
Requires:	php
Requires:	php-pcre
Requires:	php-imap
Requires:	php-domxml
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prefix:		/home/services/httpd/html

%define		_ismaildir	/home/services/httpd/html/ISMail

%description
This package contains ISMail, a webmail system for modern browsers.

%prep
%setup -q -n %{name}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ismaildir}
mv ISMail/include/ismail.conf.sample ISMail/include/ismail.conf
mv ISMail/include/istheme.conf.sample ISMail/include/istheme.conf

cp -av ISMail/* $RPM_BUILD_ROOT%{_ismaildir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BSD  CHANGELOG  CREDITS  docs.html  examples

%dir %{_ismaildir}
%dir %{_ismaildir}/include
%config %{_ismaildir}/include/*.conf
%{_ismaildir}/include/*.php
%{_ismaildir}/include/*.class
%{_ismaildir}/include/*.xml
%{_ismaildir}/*.php
%{_ismaildir}/xtree
%{_ismaildir}/locale
%{_ismaildir}/graphics
%attr(730,root,http) %dir %{_ismaildir}/users
