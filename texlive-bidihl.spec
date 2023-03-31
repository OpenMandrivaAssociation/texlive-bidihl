Name:		texlive-bidihl
Version:	37795
Release:	2
Summary:	Experimental bidi-aware text highlighting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bidihl
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidihl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidihl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Experimental bidi-aware text highlighting.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/bidihl
%doc %{_texmfdistdir}/doc/xelatex/bidihl

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
