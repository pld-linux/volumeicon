Summary:	Lightweight volume control for the system tray
Summary(pl.UTF-8):	Lekka regulacja głośności w zasobniku systemowym
Name:		volumeicon
Version:	0.5.1
Release:	1
License:	GPL-3.0
Group:		X11/Applications/Sound
URL:		https://github.com/Maato/volumeicon
Source0:	https://github.com/Maato/volumeicon/archive/refs/tags/%{version}.tar.gz
# Source0-md5:	edbc503f2ead5706d3c388f2b3608a37
Source1:	%{name}.desktop
BuildRequires:	alsa-lib-devel
BuildRequires:	gtk+3-devel
BuildRequires:	intltool
BuildRequires:	keybinder-devel
BuildRequires:	libnotify-devel >= 0.5.0

%description
Volume Icon aims to be a lightweight volume control that sits in your
system tray.

Features:
- Change volume by scrolling on the systray icon
- Ability to choose which channel to control
- Configurable stepsize
- Several icon themes
- Configurable external mixer
- Volume slider
- Hotkey support

%description -l pl.UTF-8
Ikona głośności ma być lekkim regulatorem głośności, który znajduje
się w zasobniku systemowym.

Cechy:
- Zmiana głośności, poprzez przewijanie ikony na pasku zadań
- Możliwość wyboru kanału do kontrolowania
- Konfigurowalny rozmiar skoku
- Kilka motywów ikon
- Konfigurowalny mikser zewnętrzny
- Suwak głośności
- Obsługa klawiszy skrótów

%prep
%setup -q

%build
sh autogen.sh
%configure \
	--enable-notify \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/
%find_lang %{name}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog COPYING
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/xdg/autostart/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT
