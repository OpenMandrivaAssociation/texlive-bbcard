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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Three jiffy packages for creating cards of various sorts with MetaPost.

