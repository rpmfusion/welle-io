Name:           welle-io

Version:        2.2
Release:        10%{?dist}
Summary:        Receiver for DAB and DAB+ broadcast radio

License:        GPLv2+
URL:            https://www.welle.io/
Source0:        https://github.com/AlbrechtL/welle.io/archive/v%{version}/%{name}-%{version}.tar.gz

# Basic build dependencies
BuildRequires:  cmake
BuildRequires:  gcc-c++
# Freedesktop build dependencies
BuildRequires:  desktop-file-utils
# Qt build dependencies
BuildRequires:  qt5-qtcharts-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtquickcontrols2-devel
# SDR hardware interface dependencies
BuildRequires:  SoapySDR-devel
BuildRequires:  rtl-sdr-devel
# Signal processing & codecs
BuildRequires:  fftw-devel
BuildRequires:  lame-devel
BuildRequires:  mpg123-devel
# faad2 is in rpmfusion
BuildRequires:  faad2-devel

%description
Receive digital audio broadcasts with your computer: welle.io is an open source
DAB and DAB+ software defined radio (SDR) with direct support for RTL-SDR and
other SDR hardware through SoapySDR. It supports high DPI and touch displays and
it runs even on cheap computers.


%prep
%autosetup -n welle.io-%{version}
rm -rf src/libs/faad2
rm -rf src/libs/mpg123

%build
%cmake -DSOAPYSDR=1 -DRTLSDR=1
%cmake_build

%check
%ctest


%install
%cmake_install
desktop-file-install \
    --add-category="AudioVideo" \
    --delete-original \
    --dir=%{buildroot}%{_datadir}/applications \
    %{buildroot}/%{_datadir}/applications/welle-io.desktop

%files
%license COPYING
%{_bindir}/welle-io
%{_bindir}/welle-cli
%{_datadir}/applications/welle-io.desktop
%{_datadir}/icons/hicolor/*/apps/welle-io.png
%{_datadir}/welle-io/

%doc README.md AUTHORS THANKS

%changelog
* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 2.2-10
- Changed welle-io/html directory ownership structure

* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 2.2-9
- Unbundled faad2 and mpg123

* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 2.2-8
- use %%autosetup instead of %%setup to reduce friction in future patching
  efforts

* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 2.2-7
- Changed Source0 URL to release archive

* Sun Feb 28 2021 Marcus Müller <marcus@hostalia.de> - 2.2-6
- removed Group: macro
- used macro'd target directories
- desktop-file-install .desktop file

* Sat Feb 27 2021 Marcus Müller <marcus@hostalia.de> - 2.2-5
- coherent version naming in changelog

* Sat Feb 27 2021 Marcus Müller <marcus@hostalia.de> - 2.2-4
- add qt5-qtmultimedia as build dependency

* Sat Feb 27 2021 Marcus Müller <marcus@hostalia.de> - 2.2-3
- add qt5-qtquickcontrol2 as build dependency

* Sat Feb 27 2021 Marcus Müller <marcus@hostalia.de> - 2.2-2
- Remove qt5-devel BuildRequire, as it upsets koji, and should be in
  qt5-qtcharts-devel

* Sat Feb 27 2021 Marcus Müller <marcus@hostalia.de> - 2.2-1
- Use current upstream version
- Use cmake-specific macros
- correct usage of setup
- license, license macro
- linted description, summmary, changelog

* Tue Dec 25 2018 Dick Marinus <dick@mrns.nl> - v2.0_beta1-3
- Dutch translations

* Tue Dec 25 2018 Dick Marinus <dick@mrns.nl> - v2.0_beta1-2
- Dutch translations

* Fri Dec 21 2018 Dick Marinus <dick@mrns.nl> - v2.0_beta1-1
- Update to v2.0_beta1

* Sat Dec 15 2018 Dick Marinus <dick@mrns.nl> - v2.0_beta1_4_ga90b66a-1
- Update to v2.0_beta1_4_ga90b66a

* Fri Nov 9 2018 Dick Marinus <dick@mrns.nl> - V1.0_566_ga771bec-1
- Update to V1.0_566_ga771bec

* Sat Oct 20 2018 Dick Marinus <dick@mrns.nl> - V1.0_548_gc31208d-1
- Update to V1.0_548_gc31208d

* Sat Aug 25 2018 Dick Marinus <dick@mrns.nl> - V1.0_426_g9c543d4-1
- Update to V1.0_426_g9c543d4

* Sat Jul 21 2018 Dick Marinus <dick@mrns.nl> - V1.0_363_g8813ebc
- Update to V1.0_363_g8813ebc

* Wed Jul 11 2018 Dick Marinus <dick@mrns.nl> - V1.0_353_g4b10de9-1
- Update to V1.0_353

* Fri Jul 06 2018 Dick Marinus <dick@mrns.nl> - V1.0_351_gae7d895-2
- Install icon and html files

* Sun Jul 01 2018 Dick Marinus <dick@mrns.nl> - 1.0-1
- Initial version
