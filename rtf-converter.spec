Summary:	Converts RTF files to HTML
Summary(pl.UTF-8):	Konwerter plików RTF do formatu HTML
Name:		rtf-converter
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://www.kaitiaki.org.nz/download/%{name}_%{version}.tar.gz
# Source0-md5:	224c2855e68d1aea5c4f0230cbc1879b
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-includes.patch
URL:		http://www.kaitiaki.org.nz/download/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program is intended for command-line conversion of RTF to HTML. It
produces only the HTML body code which will need to be wrapped in BODY
tags and given an HTML header. It attempts to produce HTML 4.0
(strict) compliant html code.

%description -l pl.UTF-8
Program jest przeznaczony do konwersji plików RTF do HTML. Jako wynik
otrzymujemy treść dokumentu, który należy otoczyć tagami BODY i
odpowiednimi nagłówkami HTML. Program stara się generować kod zgodny
z HTML 4.0 (strict).

%prep
%setup -q -n rtf
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(755,root,root) %{_bindir}/rtf-converter
