%bcond_with bootstrap
%global packname  AnnotationDbi
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.16.16
Release:          2
Summary:          Annotation Database Interface
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
Requires:         R-methods R-utils R-Biobase R-DBI R-RSQLite R-IRanges
Requires:         R-XML R-RCurl R-RUnit
%if %{without bootstrap}
Requires:         R-hgu95av2.db R-GO.db R-human.db0 R-hgu95av2cdf
Requires:         R-org.Sc.sgd.db R-org.At.tair.db R-affy R-KEGG.db
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    R-utils R-Biobase R-methods R-utils R-Biobase R-DBI
BuildRequires:    R-RSQLite R-IRanges R-XML R-RCurl R-RUnit 
%if %{without bootstrap}
BuildRequires:    R-hgu95av2.db R-GO.db R-human.db0 R-hgu95av2cdf
BuildRequires:    R-org.Sc.sgd.db R-org.At.tair.db R-affy R-KEGG.db
%endif

%description
Provides user interface and database connection code for annotation data
packages using SQLite data storage.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%doc %{rlibdir}/%{packname}/NOTES-Herve
%doc %{rlibdir}/%{packname}/TODO
%{rlibdir}/%{packname}/AnnDbPkg-templates
%{rlibdir}/%{packname}/DBschemas
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/ProbePkg-template
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/extdata
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests
