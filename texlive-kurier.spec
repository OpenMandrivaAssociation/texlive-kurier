# revision 19612
# category Package
# catalog-ctan /fonts/kurier
# catalog-date 2010-08-03 20:49:06 +0200
# catalog-license gfsl
# catalog-version 0.995b
Name:		texlive-kurier
Version:	0.995b
Release:	10
Summary:	A two-element sans-serif typeface
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/kurier
License:	GFSL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kurier.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kurier.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Kurier is a two-element sans-serif typeface. It was designed
for a diploma in typeface design at the Warsaw Academy of Fine
Arts under the supervision of Roman Tomaszewski. This
distribution contains a significantly extended set of
characters covering the following modern alphabets: latin
(including Vietnamese), Cyrillic and Greek as well as a number
of additional symbols (including mathematical symbols). The
fonts are prepared in Type 1 and OpenType formats. For use with
TeX the following encoding files have been prepared: T1 (ec),
T2 (abc), and OT2--Cyrillic, T5 (Vietnamese), OT4, QX, texansi
and--nonstandard (IL2 for the Czech fonts), as well as
supporting macros and files defining fonts for LaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierb.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierbi.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercb.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercbi.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierch.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierchi.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercl.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercli.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercm.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercmi.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercr.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriercri.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierh.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierhi.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierl.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierli.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierm.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kuriermi.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierr.afm
%{_texmfdistdir}/fonts/afm/nowacki/kurier/kurierri.afm
%{_texmfdistdir}/fonts/enc/dvips/kurier/cs-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/cs-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/ec-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/ec-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/ex-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/greek-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/l7x-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/l7x-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/mi-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/qx-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/qx-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/rm-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/rm-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/sy-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/t2a-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/t2b-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/t2c-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/t5-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/t5-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/texnansi-kurier-sc.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/texnansi-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/ts1-kurier.enc
%{_texmfdistdir}/fonts/enc/dvips/kurier/wncy-kurier.enc
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-cs.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-ec.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-ex.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-greek.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-l7x.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-mi.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-qx.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-rm.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-sy.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-t2a.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-t2b.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-t2c.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-t5.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-texnansi.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-ts1.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier-wncy.map
%{_texmfdistdir}/fonts/map/dvips/kurier/kurier.map
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/Kurier-Bold.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/Kurier-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/Kurier-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/Kurier-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCond-Bold.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCond-BoldItalic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCond-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCond-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCondHeavy-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCondHeavy-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCondLight-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCondLight-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCondMedium-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierCondMedium-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierHeavy-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierHeavy-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierLight-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierLight-Regular.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierMedium-Italic.otf
%{_texmfdistdir}/fonts/opentype/nowacki/kurier/KurierMedium-Regular.otf
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/cs-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ec-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ex-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/greek-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/l7x-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/mi-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/qx-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/rm-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kurierbz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kuriercbz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kurierchz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kurierclz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kuriercmz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kuriercrz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kurierhz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kurierlz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kuriermz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/sy-kurierrz.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2a-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2b-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t2c-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/t5-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercb-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercbi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierch-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierchi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercmi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierh-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierhi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierl-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierli-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierm-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriermi-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierr-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierri-sc.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/texnansi-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/ts1-kurierri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercb.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercbi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierch.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierchi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercmi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriercri.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierh.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierhi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierl.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierli.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierm.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kuriermi.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierr.tfm
%{_texmfdistdir}/fonts/tfm/nowacki/kurier/wncy-kurierri.tfm
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierb.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierbi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercb.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercbi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierch.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierchi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercl.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercli.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercm.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercmi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercr.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriercri.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierh.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierhi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierl.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierli.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierm.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kuriermi.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierr.pfb
%{_texmfdistdir}/fonts/type1/nowacki/kurier/kurierri.pfb
%{_texmfdistdir}/tex/latex/kurier/il2kurier.fd
%{_texmfdistdir}/tex/latex/kurier/il2kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/il2kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/il2kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/kurier.sty
%{_texmfdistdir}/tex/latex/kurier/l7xkurier.fd
%{_texmfdistdir}/tex/latex/kurier/l7xkurierc.fd
%{_texmfdistdir}/tex/latex/kurier/l7xkurierl.fd
%{_texmfdistdir}/tex/latex/kurier/l7xkurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/ly1kurier.fd
%{_texmfdistdir}/tex/latex/kurier/ly1kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/ly1kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/ly1kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/omlkurier.fd
%{_texmfdistdir}/tex/latex/kurier/omlkurierc.fd
%{_texmfdistdir}/tex/latex/kurier/omlkurierl.fd
%{_texmfdistdir}/tex/latex/kurier/omlkurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/omskurier.fd
%{_texmfdistdir}/tex/latex/kurier/omskurierc.fd
%{_texmfdistdir}/tex/latex/kurier/omskurierl.fd
%{_texmfdistdir}/tex/latex/kurier/omskurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/omxkurier.fd
%{_texmfdistdir}/tex/latex/kurier/omxkurierc.fd
%{_texmfdistdir}/tex/latex/kurier/omxkurierl.fd
%{_texmfdistdir}/tex/latex/kurier/omxkurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurier.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kuriercm.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurierlcm.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurierlm.fd
%{_texmfdistdir}/tex/latex/kurier/ot1kurierm.fd
%{_texmfdistdir}/tex/latex/kurier/ot2kurier.fd
%{_texmfdistdir}/tex/latex/kurier/ot2kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/ot2kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/ot2kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/ot4kurier.fd
%{_texmfdistdir}/tex/latex/kurier/ot4kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/ot4kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/ot4kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/qxkurier.fd
%{_texmfdistdir}/tex/latex/kurier/qxkurierc.fd
%{_texmfdistdir}/tex/latex/kurier/qxkurierl.fd
%{_texmfdistdir}/tex/latex/kurier/qxkurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/t1kurier.fd
%{_texmfdistdir}/tex/latex/kurier/t1kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/t1kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/t1kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/t2akurier.fd
%{_texmfdistdir}/tex/latex/kurier/t2akurierc.fd
%{_texmfdistdir}/tex/latex/kurier/t2akurierl.fd
%{_texmfdistdir}/tex/latex/kurier/t2akurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/t2bkurier.fd
%{_texmfdistdir}/tex/latex/kurier/t2bkurierc.fd
%{_texmfdistdir}/tex/latex/kurier/t2bkurierl.fd
%{_texmfdistdir}/tex/latex/kurier/t2bkurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/t2ckurier.fd
%{_texmfdistdir}/tex/latex/kurier/t2ckurierc.fd
%{_texmfdistdir}/tex/latex/kurier/t2ckurierl.fd
%{_texmfdistdir}/tex/latex/kurier/t2ckurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/t5kurier.fd
%{_texmfdistdir}/tex/latex/kurier/t5kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/t5kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/t5kurierlc.fd
%{_texmfdistdir}/tex/latex/kurier/ts1kurier.fd
%{_texmfdistdir}/tex/latex/kurier/ts1kurierc.fd
%{_texmfdistdir}/tex/latex/kurier/ts1kurierl.fd
%{_texmfdistdir}/tex/latex/kurier/ts1kurierlc.fd
%{_texmfdistdir}/tex/plain/kurier/kurier-math.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/00readme.eng
%doc %{_texmfdistdir}/doc/fonts/kurier/00readme.pol
%doc %{_texmfdistdir}/doc/fonts/kurier/GUST-FONT-LICENSE.txt
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-info-src.zip
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-info.pdf
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-latex-cyr.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-latex-math.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-latex-pl.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-latex-t2a.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-latex-t5.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-mathtest.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/kurier-table.tex
%doc %{_texmfdistdir}/doc/fonts/kurier/manifest.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.995b-2
+ Revision: 753058
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.995b-1
+ Revision: 718788
- texlive-kurier
- texlive-kurier
- texlive-kurier
- texlive-kurier

