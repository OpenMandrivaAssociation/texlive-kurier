%global tl_name kurier
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.995b
Release:	%{tl_revision}.1
Summary:	A two-element sans-serif typeface
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/kurier
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kurier.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kurier.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Kurier is a two-element sans-serif typeface. It was designed for a
diploma in typeface design at the Warsaw Academy of Fine Arts under the
supervision of Roman Tomaszewski. This distribution contains a
significantly extended set of characters covering the following modern
alphabets: latin (including Vietnamese), Cyrillic and Greek as well as a
number of additional symbols (including mathematical symbols). The fonts
are prepared in Type 1 and OpenType formats. For use with TeX the
following encoding files have been prepared: T1 (ec), T2 (abc), and OT2
--Cyrillic, T5 (Vietnamese), OT4, QX, texansi and--nonstandard (IL2 for
the Czech fonts), as well as supporting macros and files defining fonts
for LaTeX.

