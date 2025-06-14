subroutine example
   use mctc_env, only : wp
   use mctc_io, only : structure_type, new
   implicit none
   type(structure_type) :: mol
   real(wp), allocatable :: xyz(:, :)
   integer, allocatable :: num(:)

   num = [6, 1, 1, 1, 1]
   xyz = reshape([ &
     &  0.00000000000000_wp, -0.00000000000000_wp,  0.00000000000000_wp, &
     & -1.19220800552211_wp,  1.19220800552211_wp,  1.19220800552211_wp, &
     &  1.19220800552211_wp, -1.19220800552211_wp,  1.19220800552211_wp, &
     & -1.19220800552211_wp, -1.19220800552211_wp, -1.19220800552211_wp, &
     &  1.19220800552211_wp,  1.19220800552211_wp, -1.19220800552211_wp],&
     & [3, size(num)])

   call new(mol, num, xyz, charge=0.0_wp, uhf=0)

  ! print *,mol

   ! ...
end subroutine example

program test_example

call example

end program
