Summary:	Inside Systems webmail package
Summary(pl.UTF-8):	Webmail firmy Inside Systems
Name:		ismail
Version:	2.0
Release:	2
License:	GPL
Group:		Applications/Mail
Source0:	ftp://ftp.insidesystems.net/ismail/%{name}-%{version}.tar.bz2
# Source0-md5:	df7b88426f24250cd7ffee6f29d330b2
Source1:	%{name}-apache.conf
# from http://alexandre.alapetite.net/doc-alex/domxml-php4-php5/index.en.html
Source2:	%{name}-domxml4-to5-fixup.php
Patch0:		%{name}-php5.patch
URL:		http://www.insidesystems.net/projects/project.php?projectid=4
BuildRequires:	rpmbuild(macros) >= 1.264
Requires:	php(domxml)
Requires:	php(imap)
Requires:	php(pcre)
Requires:	php(xml)
Requires:	webapps
Requires:	webserver
Requires:	webserver(php)
Provides:	webmail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ismaildir	%{_datadir}/%{name}
%define 	_sysconfdir	/etc/%{name}
%define		_webapps	/etc/webapps
%define		_webapp		%{name}
%define		_webappsdir	%{_webapps}/%{name}

%description
This package contains ISMail, a webmail system for modern browsers.

%description -l pl.UTF-8
Ten pakiet zawiera ISMaila - system webmailowy dla nowoczesnych
przeglądarek.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ismaildir} \
	    $RPM_BUILD_ROOT{%{_sysconfdir},%{_webappsdir}}
mv ismail/include/ismail.conf.sample ismail/include/ismail.conf
mv ismail/include/istheme.conf.sample ismail/include/istheme.conf

cp -av ismail/* $RPM_BUILD_ROOT%{_ismaildir}

cp ismail/include/*.conf $RPM_BUILD_ROOT%{_sysconfdir}

ln -sf %{_sysconfdir}/ismail.conf $RPM_BUILD_ROOT%{_ismaildir}/include/ismail.conf
ln -sf %{_sysconfdir}/istheme.conf $RPM_BUILD_ROOT%{_ismaildir}/include/istheme.conf

install %{SOURCE1} $RPM_BUILD_ROOT%{_webappsdir}/apache.conf
install %{SOURCE1} $RPM_BUILD_ROOT%{_webappsdir}/httpd.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_ismaildir}/include/datastores/domxml4-to5-fixup.php

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

%files
%defattr(644,root,root,755)
%doc BSD CHANGELOG CREDITS docs.html examples
%dir %{_sysconfdir}
%{_sysconfdir}/*.conf
%dir %{_ismaildir}
%dir %{_ismaildir}/include
%{_webappsdir}
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
