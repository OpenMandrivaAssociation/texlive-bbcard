%global tl_name bbcard
%global tl_revision 19440

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bullshit bingo, calendar and baseball-score cards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/bbcard
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbcard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bbcard.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Three jiffy packages for creating cards of various sorts with MetaPost.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/metapost
%dir %{_datadir}/texmf-dist/doc/metapost
%dir %{_datadir}/texmf-dist/metapost/bbcard
%dir %{_datadir}/texmf-dist/doc/metapost/bbcard
%doc %{_datadir}/texmf-dist/doc/metapost/bbcard/README.TEXLIVE
%doc %{_datadir}/texmf-dist/doc/metapost/bbcard/README.bbcard
%doc %{_datadir}/texmf-dist/doc/metapost/bbcard/README.calendar
%doc %{_datadir}/texmf-dist/doc/metapost/bbcard/README.scorecard
%{_datadir}/texmf-dist/metapost/bbcard/bbcard.mp
%{_datadir}/texmf-dist/metapost/bbcard/breakwidth.mp
%{_datadir}/texmf-dist/metapost/bbcard/calendar.mp
%{_datadir}/texmf-dist/metapost/bbcard/scorecard.mp
