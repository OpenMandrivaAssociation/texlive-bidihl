%global tl_name bidihl
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1c
Release:	%{tl_revision}.1
Summary:	Experimental bidi-aware text highlighting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/bidihl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidihl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bidihl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Experimental bidi-aware text highlighting.

