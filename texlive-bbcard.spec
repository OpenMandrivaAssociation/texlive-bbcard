# revision 19440
# category Package
# catalog-ctan /graphics/metapost/contrib/macros/bbcard
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license pd
# catalog-version undef
Name:		texlive-bbcard
Version:	20080817
Release:	1
Summary:	Bullshit bingo, calendar and baseball-score cards
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/bbcard
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbcard.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bbcard.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Three jiffy packages for creating cards of various sorts with
MetaPost.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
