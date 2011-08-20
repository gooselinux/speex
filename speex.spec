Summary:	A voice compression format (codec)
Name:		speex
Version:	1.2
%define rc_ver	rc1
Release:	0.12.%{rc_ver}.1%{?dist}
License:	BSD
Group:		System Environment/Libraries
URL:		http://www.speex.org/
Source0:	http://downloads.xiph.org/releases/speex/%{name}-%{version}%{rc_ver}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libogg-devel

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

%package devel
Summary: 	Development package for %{name}
Group: 		Development/Libraries
Requires: 	%{name} = %{version}-%{release}
Requires: 	pkgconfig

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{name}

%package tools
Summary:	The tools package for %{name}
Group:		Applications/Multimedia
Requires:	%{name} = %{version}-%{release}

%description tools
Speex is a patent-free compression format designed especially for
speech. This package contains tools files and user's manual for %{name}.

%prep
%setup -q -n %{name}-%{version}%{rc_ver}

%build
%configure --disable-static
# Remove rpath from speexenc and speexdec
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_docdir}/speex/manual.pdf

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING TODO ChangeLog README NEWS
%{_libdir}/libspeex*.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/manual.pdf
%{_includedir}/speex
%{_datadir}/aclocal/speex.m4
%{_libdir}/pkgconfig/speex*.pc
%{_libdir}/libspeex*.so
%exclude %{_libdir}/libspeex*.la

%files tools
%defattr(-,root,root,-)
%{_bindir}/speexenc
%{_bindir}/speexdec
%{_mandir}/man1/speexenc.1*
%{_mandir}/man1/speexdec.1*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2-0.12.rc1.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.12.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-0.11.rc1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 24 2008 Miroslav Lichvar <mlichvar@redhat.com> - 1.2-0.10.rc1
- update to 1.2rc1
- move manual.pdf to -devel

* Tue May 13 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-0.9.beta3
- polishing review (many thanks to Matthias Saou)

* Fri Apr 25 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-0.8.beta3
- 226428 review

* Tue Apr 15 2008 Tomas Hoger <thoger@redhat.com> - 1.2-0.7.beta3
- Security update: Add mode checks to speex_packet_to_header() to protect
  applications using speex library and not having proper checks
  (CVE-2008-1686, #441239, https://trac.xiph.org/changeset/14701)

* Mon Mar 31 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-0.6.beta3
- 439284 add owner to %%{_defaultdocdir}/speex

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-0.5.beta3
- Autorebuild for GCC 4.3

* Thu Jan 24 2008 Marcela Maslanova <mmaslano@redhat.com> - 1.2-0.4.beta3
- update to beta 3
- review: rhbz#226428

* Tue Sep 18 2007 - Bastien Nocera <bnocera@redhat.com> - 1.2-0.3.beta2
- Update to Beta 2

* Tue Oct 24 2006 Matthias Clasen <mclasen@redhat.com> - 1.2-0.2.beta1
- Rebuild 

* Tue Oct 24 2006 Matthias Clasen <mclasen@redhat.com> - 1.2-0.1.beta1
- Update to 1.2beta1
- Require pkgconfig in the -devel package

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-2.1
- rebuild

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 1.0.5-2
- rebuild for -devel deps

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.5-1.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 09 2005 John (J5) Palmieri <johnp@redhat.com> -1.0.5-1
- Update to 1.0.5

* Wed Mar 02 2005 John (J5) Palmieri <johnp@redhat.com> -1.0.4-5
- rebuild for gcc 4.0

* Mon Oct 18 2004 Miloslav Trmac <mitr@redhat.com> - 1.0.4-4
- Fix version in pkg-config file (#135987, patch by Michael Schwendt)

* Wed Aug 11 2004 Tim Waugh <twaugh@redhat.com> 1.0.4-3
- Fixed underquoted m4 definition.

* Fri Jul 30 2004 Colin Walters <walters@redhat.com> 1.0.4-2
- Include /usr/include/speex directory, thanks
  Nils Philippsen.

* Thu Jul 29 2004 Colin Walters <walters@redhat.com>
- Update to 1.0.4.
- Include /usr/include/speex
- Include speex.pc

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Dec 12 2003 Bill Nottingham <notting@redhat.com> 1.0.3-1
- build 1.0.3, adapt specfile from linva.org

* Thu Nov 20 2003 Dams <anvil[AT]livna.org> 0:1.0.3-0.fdr.1
- Updated to 1.0.3

* Tue Sep 30 2003 Dams <anvil[AT]livna.org> 0:1.0.2-0.fdr.1
- Updated to 1.0.2

* Mon Sep 15 2003 Dams <anvil[AT]livna.org> 0:1.0.1-0.fdr.3
- README doc file is no more +x

* Tue Sep  9 2003 Dams <anvil[AT]livna.org> 0:1.0.1-0.fdr.2
- Added missing scriplets (ldconfig)

* Sat Aug 16 2003 Dams <anvil[AT]livna.org> 
- Initial build.
