%{?scl:%scl_package perl-autodie}

# Run optional test
%if ! (0%{?scl:1})
%bcond_without perl_autodie_enables_optional_test
%else
%bcond_with perl_autodie_enables_optional_test
%endif

Name:           %{?scl_prefix}perl-autodie
Version:        2.29
Release:        452%{?dist}
Summary:        Replace functions with ones that succeed or die
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/autodie
Source0:        https://cpan.metacpan.org/authors/id/P/PJ/PJF/autodie-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time:
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Exporter) >= 5.57
BuildRequires:  %{?scl_prefix}perl(Fcntl)
%if !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(IPC::System::Simple) >= 0.12
%endif
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(parent)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Sub::Identify is optional
BuildRequires:  %{?scl_prefix}perl(Tie::RefHash)
# Tests:
# English not used
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(File::Temp)
BuildRequires:  %{?scl_prefix}perl(FindBin)
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(IO::Handle)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(open)
# Pod::Coverage::TrustPod not used
BuildRequires:  %{?scl_prefix}perl(Socket)
# Test::Kwalitee not used
BuildRequires:  %{?scl_prefix}perl(Test::More)
# Test::Perl::Critic not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Optional tests:
%if %{with perl_autodie_enables_optional_test} && !%{defined perl_bootstrap}
BuildRequires:  %{?scl_prefix}perl(BSD::Resource)
BuildRequires:  %{?scl_prefix}perl(Import::Into) >= 1.002004
%endif
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(B)
Requires:       %{?scl_prefix}perl(Fcntl)
Requires:       %{?scl_prefix}perl(POSIX)
# Optional:
%if !%{defined perl_bootstrap}
# IPC::System::Simple dependency requested, bug #1183231
Requires:  %{?scl_prefix}perl(IPC::System::Simple) >= 0.12
%endif

# Remove falsely detected perl(lib)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\(lib\\)$

%description
The "autodie" and "Fatal" pragma provides a convenient way to replace
functions that normally return false on failure with equivalents that throw an
exception on failure.

However "Fatal" has been obsoleted by the new autodie pragma. Please use
autodie in preference to "Fatal".

%prep
%setup -q -n autodie-%{version}
find -type f -exec chmod -x {} +

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=$RPM_BUILD_ROOT%{?scl:'}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc AUTHORS Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Jan 07 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-452
- Re-rebuild of bootstrapped packages

* Fri Dec 20 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-451
- SCL

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-440
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-439
- Perl 5.30 re-rebuild of bootstrapped packages

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-438
- Increase release to favour standalone package

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-419
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-418
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-417
- Perl 5.28 re-rebuild of bootstrapped packages

* Tue Jun 26 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-416
- Increase release to favour standalone package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-396
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-395
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 07 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-394
- Perl 5.26 re-rebuild of bootstrapped packages

* Sat Jun 03 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-393
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-367
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-366
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.29-365
- Increase release to favour standalone package

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 09 2015 Petr Pisar <ppisar@redhat.com> - 2.29-1
- 2.29 bump

* Mon Jun 22 2015 Petr Pisar <ppisar@redhat.com> - 2.28-1
- 2.28 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.27-2
- Perl 5.22 re-rebuild of bootstrapped packages

* Wed Jun 10 2015 Petr Pisar <ppisar@redhat.com> - 2.27-1
- 2.27 bump

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.26-3
- Perl 5.22 rebuild

* Mon Jan 19 2015 Petr Pisar <ppisar@redhat.com> - 2.26-2
- Run-require IPC::System::Simple for fatalizing system() (bug #1183231)

* Mon Jan 05 2015 Petr Pisar <ppisar@redhat.com> - 2.26-1
- 2.26 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.25-4
- Perl 5.20 re-rebuild of bootstrapped packages

* Tue Aug 26 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.25-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Petr Pisar <ppisar@redhat.com> - 2.25-1
- 2.25 bump

* Mon Mar 31 2014 Petr Pisar <ppisar@redhat.com> - 2.24-1
- 2.24 bump

* Thu Jan 30 2014 Petr Pisar <ppisar@redhat.com> - 2.23-1
- 2.23 bump

* Mon Sep 23 2013 Petr Pisar <ppisar@redhat.com> - 2.22-1
- 2.22 bump

* Thu Sep 12 2013 Petr Pisar <ppisar@redhat.com> - 2.21-1
- 2.21 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2.20-4
- Perl 5.18 re-rebuild of bootstrapped packages

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.20-2
- Perl 5.18 rebuild

* Mon Jul 01 2013 Petr Pisar <ppisar@redhat.com> - 2.20-1
- 2.20 bump

* Wed Mar 06 2013 Petr Pisar <ppisar@redhat.com> - 2.16-1
- 2.16 bump

* Thu Feb 14 2013 Petr Pisar <ppisar@redhat.com> 2.13-1
- Specfile autogenerated by cpanspec 1.78.
