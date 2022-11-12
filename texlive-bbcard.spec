Name:		texlive-bbcard
Version:	19440
Release:	1
Summary:	Bullshit bingo, calendar and baseball-score cards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/bbcard
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbcard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbcard.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Three jiffy packages for creating cards of various sorts with
MetaPost.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/bbcard/bbcard.mp
%{_texmfdistdir}/metapost/bbcard/breakwidth.mp
%{_texmfdistdir}/metapost/bbcard/calendar.mp
%{_texmfdistdir}/metapost/bbcard/scorecard.mp
%doc %{_texmfdistdir}/doc/metapost/bbcard/README.TEXLIVE
%doc %{_texmfdistdir}/doc/metapost/bbcard/README.bbcard
%doc %{_texmfdistdir}/doc/metapost/bbcard/README.calendar
%doc %{_texmfdistdir}/doc/metapost/bbcard/README.scorecard

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
