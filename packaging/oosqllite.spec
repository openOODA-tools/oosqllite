Name:           oosqllite
Version:        0.1.0
Release:        1%{?dist}
Summary:        Zero-dependency embedded SQL query runner querying stdin streams in memory.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oosqllite
Source0:        oosqllite-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oosqllite is a sovereign, capability-bounded EMBEDDED SQL written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oosqllite
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oosqllite-uninstall

%files
/usr/bin/oosqllite
/usr/bin/oosqllite-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
