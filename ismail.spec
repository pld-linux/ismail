Summary:	Inside Systems webmail package
Summary(pl):	Webmail firmy Inside Systems
Name:		ISMail
Version:	1.7.3
Release:	0.1
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.verbotenplanet.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	482c9c3eda83714187c3b2c52a0c4f9d
URL:		http://www.insidesystems.net/projects/project.php?projectid=4
Requires:	php
Requires:	php-pcre
Requires:	php-imap
Requires:	php-domxml
Requires:	webserver
Provides:	webmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prefix:		/home/services/httpd/html

%define		_ismaildir	/home/services/httpd/html/ISMail

%description
This package contains ISMail, a webmail system for modern browsers.

%description -l pl
Ten pakiet zawiera ISMaila - system webmailowy dla nowoczesnych
przegl±darek.

%prep
%setup -q -n %{name}

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
%config(noreplace) %verify(not size mtime md5) %{_ismaildir}/include/*.conf
%{_ismaildir}/include/*.php
%{_ismaildir}/include/*.class
%{_ismaildir}/include/*.xml
%{_ismaildir}/*.php
%{_ismaildir}/xtree
%{_ismaildir}/locale
%{_ismaildir}/graphics
%attr(730,root,http) %dir %{_ismaildir}/users
