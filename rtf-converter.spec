Summary:	Converts RTF files to HTML
Summary(pl):	Konwerter plików RTF do formatu HTML
Name:		rtf-converter
Version:	1.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.kaitiaki.org.nz/download/%{name}_%{version}.tar.gz
# Source0-md5:	224c2855e68d1aea5c4f0230cbc1879b
URL:		http://www.kaitiaki.org.nz/download/
Patch0:		%{name}-cflags.patch
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program is intended for command-line conversion of RTF to HTML. It
produces only the HTML body code which will need to be wrapped in BODY
tags and given an HTML header. It attempts to produce HTML 4.0
(strict) compliant html code.

%description -l pl
Program jest przeznaczony do konwersji plików RTF do HTML. Jako wynik
otrzymujemy tre¶æ dokumentu, który nale¿y otoczyæ tagami BODY i
odpowiednimi nag³ówkami HTML. Program stara siê generowaæ kod zgodny
z HTML 4.0 (strict).

%prep
%setup -q -n rtf
%patch0 -p1

%build
%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%attr(755,root,root) %{_bindir}/rtf-converter
